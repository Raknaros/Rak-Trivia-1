from bs4 import BeautifulSoup as bs
import pandas as pd
import zipfile
import os

xmlfiles = os.listdir('D:\\python\\xmls')
dfImport=pd.DataFrame(columns=["descripcion","cantidad","precio_unitario","precio_unitario_incigv","precio_total","igv_total","tasa_igv","fecha_emision","serie_comprobante","numero_correlativo","tipo_documento_emisor","numero_documento_emisor","tipo_documento_receptor","numero_documento_receptor","valor","igv","tipo_moneda","forma_pago"])
for a in xmlfiles:
    with zipfile.ZipFile('D:\\python\\xmls\\' + a, mode="r") as archive:
        file=archive.read((archive.namelist())[0]).decode(encoding="latin_1")
        content="".join(file)
        bs_content=bs(content,'xml')
        if "FACTURA" in a:
            filas = []
            filas.append(bs_content.find("cbc:InvoiceTypeCode").text) #Tipo de comprobante
            filas.append((bs_content.find("cbc:ID").text.split("-"))[0]) #Serie del comprobante
            filas.append((bs_content.find("cbc:ID").text.split("-"))[1]) #Numero del comprobante
            infoProveedor = bs_content.find("cac:AccountingSupplierParty") #Informacion de emisor/proveedor
            filas.append(infoProveedor.find("cbc:ID").get("schemeID")) #tipo de documento emisor/proveedor
            filas.append(infoProveedor.find("cbc:ID").text) #numero de documento emisor/proveedor
            infoCliente = bs_content.find("cac:AccountingCustomerParty") # Informacion de remitente/cliente
            filas.append(infoCliente.find("cbc:ID").get("schemeID")) #tipo de documento remitente/cliente
            filas.append(infoCliente.find("cbc:ID").text) #numero de documento remitente/cliente
            taxInfo = bs_content.find("cac:TaxTotal") #Informacion de impuestos
            filas.append(taxInfo.find("cbc:TaxableAmount").text) #subtotal
            filas.append(taxInfo.find("cbc:TaxAmount").text) #igv total
            filas.append(taxInfo.find("cbc:TaxAmount").get("currencyID")) #tipo de moneda
            #totalInfo = bs_content.find("cac:LegalMonetaryTotal")
            documentoReferencia = bs_content.find("cac:DespatchDocumentReference") #Informacion de documentos de referencia
            try:
                tipoReferencia=documentoReferencia.find("cbc:DocumentTypeCode").text #tipo de documento de referencia
                serieReferencia=(documentoReferencia.find("cbc:ID").text.split(" - "))[0] #serie de documento de referencia
                numeroReferencia=(documentoReferencia.find("cbc:ID").text.split(" - "))[1] #numero de documento de referencia
            except: pass
            try: 
                formaPago = bs_content.find_all("cac:PaymentTerms") #Informacion de forma de pago y cuotas
                tipoPago=formaPago[0].find("cbc:PaymentMeansID").text #Forma de pago   
                formaPago.pop(0)
            except:
                tipoPago="Contado"
            finally: filas.append(tipoPago)
            itemsInfo = bs_content.find_all("cac:InvoiceLine") #Descripcion de la factura
            for item in itemsInfo:
                lista = []
                lista.append((item.find("cbc:Description").text).replace("Ã¯Â¿Â½","Ñ")) #Descripcion corrigiendo la Ñ
                lista.append(item.find("cbc:InvoicedQuantity").text) #Cantidad
                precios=item.find_all("cbc:PriceAmount")
                lista.append(precios[1].text) #Precio unitario sin IGV
                lista.append(precios[0].text) #Precio unitario incluido IGV
                lista.append(item.find("cbc:LineExtensionAmount").text) #Subtotal de articulo
                lista.append(item.find("cbc:TaxAmount").text) #IGV total del articulo
                IGvs=item.find_all("cbc:Percent")
                lista.append(IGvs[1].text) #Porcentaje de IGV
                filas.append(lista)
            cuoTas=[]
            columnasCuotas=[]
            if tipoPago == "Credito":   
                for pago in formaPago:
                    cuoTas.append(pago.find("cbc:PaymentDueDate").text) #Fecha cuota
                    cuoTas.append(pago.find("cbc:Amount").text) #Importe cuota
                fechaCuota=1
                importeCuota=1
                for i in range(len(cuoTas)): 
                    if (i%2) == 0:
                        columnasCuotas.append("fecha_cuota"+str(fechaCuota))
                        fechaCuota+=1
                    else:
                        columnasCuotas.append("importe_cuota"+str(importeCuota))
                        importeCuota+=1
            paGos=pd.DataFrame([cuoTas],columns=columnasCuotas)
            numListas=sum(isinstance(x, list) for x in filas)
            newFila=pd.DataFrame(filas[11:]).merge(pd.DataFrame(filas[:11]).T, how='cross').set_axis(["descripcion","cantidad","precio_unitario","precio_unitario_incigv","precio_total","igv_total","tasa_igv","fecha_emision","serie_comprobante","numero_correlativo","tipo_documento_emisor","numero_documento_emisor","tipo_documento_receptor","numero_documento_receptor","valor","igv","tipo_moneda","forma_pago"], axis=1)
            newFila=newFila.merge(paGos, how='cross')
            dfImport=pd.concat([dfImport,newFila],ignore_index=True)
            dfImport.to_excel("D:\\parseractual.xlsx")
        elif "NOTA_CREDITO" in a:
            filas = []
            filas.append((bs_content.find("cbc:ID").text.split("-"))[0]) #Serie del comprobante
            filas.append((bs_content.find("cbc:ID").text.split("-"))[1]) #Numero del comprobante
            infoProveedor = bs_content.find("cac:AccountingSupplierParty") #Informacion de emisor/proveedor
            filas.append(infoProveedor.find("cbc:ID").get("schemeID")) #tipo de documento emisor/proveedor
            filas.append(infoProveedor.find("cbc:ID").text) #numero de documento emisor/proveedor
            infoCliente = bs_content.find("cac:AccountingCustomerParty") # Informacion de remitente/cliente
            filas.append(infoCliente.find("cbc:ID").get("schemeID")) #tipo de documento remitente/cliente
            filas.append(infoCliente.find("cbc:ID").text) #numero de documento remitente/cliente
















#import xml.etree.ElementTree as ET
#contador = 0
#z = {}
#tree = ET.parse('D:\\python\\xmls\\FACTURAE001-32620553737100.xml')
#root = tree.getroot()
#for child in root.iter():
#    contador += 1
#    if child.text is not None:
#       z[str(contador) + child.tag[child.tag.find('}')+1:]] = child.text
#print(z)

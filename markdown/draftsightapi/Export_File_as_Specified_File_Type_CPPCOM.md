---
title: "Export File as Specified File Type Example (COM native C++)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Export_File_as_Specified_File_Type_CPPCOM.htm"
---

# Export File as Specified File Type Example (COM native C++)

This code snippet shows how to export a file to a specified file type.

```vb
//Get IDocumentExporter object
     IDocumentExporterPtr dsDocExporter = dsDoc->GetDocumentExporter();
     if( NULL == dsDocExporter )
     {
         ::AfxMessageBox( L"Failed to get IDocumentExporter object of the current document." );

         return;
     }

     //Display SaveAs dialog to export file to the selected format
     CString filesFilter = L"Bitmap (*.bmp)|*.bmp|Windows Enhanced Metafile (*.emf)|*.emf|JPEG (*.jpg)|*.jpg|PNG (*.png)|*.png|Slide (*.sld)|*.sld|Scalable Vector Graphics Format (*.svg)|*.svg|Tag Image Format (*.tif)|*.tif|Stereolithography (*.stl)|*.stl||";
     CStringArray strExtList;
     strExtList.Add( L".bmp" );
     strExtList.Add( L".emf" );
     strExtList.Add( L".jpg" );
     strExtList.Add( L".png" );
     strExtList.Add( L".sld" );
     strExtList.Add( L".svg" );
     strExtList.Add( L".tif" );
     strExtList.Add( L".stl" );

     CFileDialog fileSaveDialog ( FALSE, NULL, L"ExportedFile", OFN_OVERWRITEPROMPT, filesFilter );

     INT_PTR result = fileSaveDialog.DoModal();
     if( IDOK == result )
     {
         DWORD nFilterIndex = fileSaveDialog.m_ofn.nFilterIndex;
         CString fullPathName = fileSaveDialog.GetPathName() + strExtList[nFilterIndex -1];
         bstr_t expFileName ( fullPathName );

         //Get export type from file name extension
         ExportType exportType = GetExportTypeFromFileExt( GetFileExtension( fullPathName ) );
         VARIANT_BOOL bSuccess = VARIANT_FALSE;

         switch (exportType)
         {
         case eBMP:
             {
                 //Export to BMP image
                 dsDocExporter->ExportToBmp( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to BMP image." );
                 }

                 break;
             }
         case eEMF:
             {
                 //Export to EMF format
                 dsDocExporter->ExportToEmf( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to EMF format." );
                 }

                 break;
             }
         case eJPG:
             {
                 //Export to JPG image
                 dsDocExporter->ExportToJpg( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to JPG image." );
                 }

                 break;
             }
         case ePNG:
             {
                 //Export to PNG image
                 dsDocExporter->ExportToPng( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to PNG image." );
                 }

                 break;
             }
         case eSLD:
             {
                 //Export to SLD format
                 dsDocExporter->ExportToSld( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to SLD format." );
                 }

                 break;
             }
         case eSVG:
             {
                 //Export to SVG format
                 dsDocExporter->ExportToSvg( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to SVG format." );
                 }

                 break;
             }
         case eTIFF:
             {
                 //Export to TIFF image
                 dsDocExporter->ExportToTiff( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to TIFF image." );
                 }

                 break;
             }
         case eSTL:
             {
                 //Export to STL format
                 dsDocExporter->ExportToStl( fullPathName.AllocSysString(), &bSuccess );
                 if( VARIANT_FALSE == bSuccess )
                 {
                     ::AfxMessageBox( L"Failed to export current document to STL format." );
                 }

                 break;
             }
         }
     }
 }

 //Method to get export type from file name extension
 ExportType CExportToCommandRunner::GetExportTypeFromFileExt( CString fileExtension )
 {
     ExportType exportType = eUndefinedExpType;

     if( fileExtension.MakeUpper() == "BMP" )
     {
         exportType = eBMP;
     }

     if( fileExtension.MakeUpper() == "EMF" )
     {
         exportType = eEMF;
     }

     if( fileExtension.MakeUpper() == "JPG" )
     {
         exportType = eJPG;
     }

     if( fileExtension.MakeUpper() == "PNG" )
     {
         exportType = ePNG;
     }

     if( fileExtension.MakeUpper() == "SLD" )
     {
         exportType = eSLD;
     }

     if( fileExtension.MakeUpper() == "SVG" )
     {
         exportType = eSVG;
     }

     if( fileExtension.MakeUpper() == "TIF" )
     {
         exportType = eTIFF;
     }

     if( fileExtension.MakeUpper() == "STL" )
     {
         exportType = eSTL;
     }

     return exportType;
 }

 CString CExportToCommandRunner::GetFileExtension(  const CString &fullPath )
 {
     CString fileExtension = L"";
     int position;

     if( (position = fullPath.ReverseFind( '.' ) ) != -1 )
     {
         fileExtension = fullPath.Right( fullPath.GetLength() - position - 1 );
     }

     return fileExtension;
 }
```

---
title: "DetachPdfDefinition Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "DetachPdfDefinition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachPdfDefinition.html"
---

# DetachPdfDefinition Method (ISketchManager)

Detaches the specified PDF definition from the drawing.

## Syntax

### Visual Basic

```vb
Function DetachPdfDefinition( _
   ByVal PdfDefinition As PdfDefinition _
) As System.Boolean
```

### C#

```csharp
System.bool DetachPdfDefinition(
   PdfDefinition PdfDefinition
)
```

### JScript

```
function DetachPdfDefinition(
   PdfDefinition : PdfDefinition
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DetachPdfDefinition(
   PdfDefinition* PdfDefinition
)
```

### C++/CLI

```cpp
System.bool DetachPdfDefinition(
   PdfDefinition^ PdfDefinition
)
```

### Parameters

- `PdfDefinition`: PDF definition

### Return Value

True if successful, false if not

## Examples

Create a C++ program in Visual Studio using the C++ snippet below, substituting `your_pdf` with the full path to a PDF file on your computer.

=======================================================================

C++ snippet attaches and detaches `your_pdf`

=============================================================================

dsCommandMessage_ptr commandline;

application->**GetCommandMessage**(&commandline);

dsRunCommandError_e error = dsRunCommand_InvalidCommand;

dsStringArray parameters;

dsLongArray parametersLong;

dsString strFile = L"`your_pdf`";

dsResType_e type = dsResType_String;

parameters.add( strFile );

parametersLong.add( type );

application->**RunCommand2**( L"_ATTACHPDF", parameters, parametersLong, true, &error );

commandline->**PrintLine**( error != dsRunCommand_Succeeded ? L"Run command failed" : L"Run command passed!" );

dsDocument_ptr document;

application->**GetActiveDocument**( &document );

dsLongArray ExternalDefinitionTypeLongArray;

dsObjectPtrArray ExternalDefinitionsArray;

document->**GetImmediateChildReferences**( &ExternalDefinitionTypeLongArray, &ExternalDefinitionsArray );

dsModel_ptr dsModel;

document->**GetModel**( &dsModel );

dsSketchManager_ptr sketchManager;

dsModel->**GetSketchManager**( &sketchManager );

dsPdfDefinition_c* pdfDefinition = ( dsPdfDefinition_c* )ExternalDefinitionsArray[ 0 ];

bool bRet;

sketchManager->**DetachPdfDefinition**( pdfDefinition, &bRet );

commandline->**PrintLine**( bRet ? L"Passed to detach Pdf" : L"Failed to detach PDF" );

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertPdf Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPdf.html)

## Availability

DraftSight 2024 SP02

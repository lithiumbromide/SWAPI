---
title: "ImportScheme Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "ImportScheme"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~ImportScheme.html"
---

# ImportScheme Method (IDimXpertPart)

Imports the tolerance scheme of the specified file to the specified configuration of this open model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ImportScheme( _
   ByVal Filename As System.String, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Filename As System.String
Dim ConfigurationName As System.String
Dim value As System.Boolean

value = instance.ImportScheme(Filename, ConfigurationName)
```

### C#

```csharp
System.bool ImportScheme(
   System.string Filename,
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
System.bool ImportScheme(
   System.String^ Filename,
   System.String^ ConfigurationName
)
```

### Parameters

- `Filename`: Full path name of the file whose tolerance scheme to import to ConfigurationName
- `ConfigurationName`: Name of the configuration in the open model document to which to import the tolerance scheme

### Return Value

True if tolerance scheme successfully imported, false if not

## VBA Syntax

See [DimXpertPart::ImportScheme](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~ImportScheme.html).

## Examples

'VBA

'1. Open a model document with a Default configuration.

'2. Edit the ImportScheme command to point to a model document with the tolerance scheme to import.

'3. Run the macro.

Option Explicit
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSchema As SldWorks.DimXpertManager
Dim swDXPart As DimXpertPart
Dim status As Boolean
Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelDocExt = swModel.Extension
Set swSchema = swModelDocExt.DimXpertManager("Default", True)
Set swDXPart = swSchema.DimXpertPart

status = swDXPart.**ImportScheme**("`Path_name`\`model_name`.SLDPRT", "Default")

End Sub

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

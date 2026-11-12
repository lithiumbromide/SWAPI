---
title: "ReferencedConfigurations Property (ISwDMExternalReferenceOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption"
member: "ReferencedConfigurations"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ReferencedConfigurations.html"
---

# ReferencedConfigurations Property (ISwDMExternalReferenceOption)

Gets the names of the configurations in the external references in the document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferencedConfigurations As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption
Dim value As System.Object

value = instance.ReferencedConfigurations
```

### C#

```csharp
System.object ReferencedConfigurations {get;}
```

### C++/CLI

```cpp
property System.Object^ ReferencedConfigurations {
   System.Object^ get();
}
```

### Property Value

Array of strings of the names of the configurations

## VBA Syntax

See [SwDMExternalReferenceOption::ReferencedConfigurations](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption~ReferencedConfigurations.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## See Also

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html)
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.html)
[ISwDMDocument15::GetExternalFeatureReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0

---
title: "BrokenStatus Property (ISwDMExternalReferenceOption2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption2"
member: "BrokenStatus"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2~BrokenStatus.html"
---

# BrokenStatus Property (ISwDMExternalReferenceOption2)

Gets whether the external references are broken in the document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BrokenStatus As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption2
Dim value As System.Object

value = instance.BrokenStatus
```

### C#

```csharp
System.object BrokenStatus {get;}
```

### C++/CLI

```cpp
property System.Object^ BrokenStatus {
   System.Object^ get();
}
```

### Property Value

Array of integers of the statuses of the external references as defined in [swDmReferenceStatus](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmReferenceStatus.html)

## VBA Syntax

See [SwDMExternalReferenceOption2::BrokenStatus](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption2~BrokenStatus.html).

## Examples

[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## Remarks

## See Also

[ISwDMExternalReferenceOption2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.html)
[ISwDMExternalReferenceOption2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption2_members.html)

## Availability

SOLIDWORKS Document Manager API 2014 SP0

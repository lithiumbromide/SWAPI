---
title: "UpdateWhereUsedReferences Property (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "UpdateWhereUsedReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html"
---

# UpdateWhereUsedReferences Property (IRenamedDocumentReferences)

Gets or sets whether to update the references to the new file name.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpdateWhereUsedReferences As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim value As System.Boolean

instance.UpdateWhereUsedReferences = value

value = instance.UpdateWhereUsedReferences
```

### C#

```csharp
System.bool UpdateWhereUsedReferences {get; set;}
```

### C++/CLI

```cpp
property System.bool UpdateWhereUsedReferences {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to update the references to the new file name, false to continue to reference the old file name

## VBA Syntax

See [RenamedDocumentReferences::UpdateWhereUsedReferences](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~UpdateWhereUsedReferences.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

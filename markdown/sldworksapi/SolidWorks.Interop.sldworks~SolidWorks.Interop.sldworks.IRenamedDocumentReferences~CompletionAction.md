---
title: "CompletionAction Property (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "CompletionAction"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~CompletionAction.html"
---

# CompletionAction Property (IRenamedDocumentReferences)

Gets or sets whether to update references to the renamed file in unopened documents.

## Syntax

### Visual Basic (Declaration)

```vb
Property CompletionAction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim value As System.Integer

instance.CompletionAction = value

value = instance.CompletionAction
```

### C#

```csharp
System.int CompletionAction {get; set;}
```

### C++/CLI

```cpp
property System.int CompletionAction {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Update references to the renamed file in unopened documents as defined in [swRenamedDocumentFinalAction_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenamedDocumentFinalAction_e.html)

## VBA Syntax

See [RenamedDocumentReferences::CompletionAction](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~CompletionAction.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

This property is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

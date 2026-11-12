---
title: "IncludeFileLocations Property (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "IncludeFileLocations"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.html"
---

# IncludeFileLocations Property (IRenamedDocumentReferences)

Gets or sets whether to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations**.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeFileLocations As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim value As System.Boolean

instance.IncludeFileLocations = value

value = instance.IncludeFileLocations
```

### C#

```csharp
System.bool IncludeFileLocations {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeFileLocations {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations**, false to not

## VBA Syntax

See [RenamedDocumentReferences::IncludeFileLocations](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~IncludeFileLocations.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

This property is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[IRenamedDocumentReferences::AddSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.html)
[IRenamedDocumentReferences::RemoveSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.html)
[IRenamedDocumentReferences::GetSearchPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0

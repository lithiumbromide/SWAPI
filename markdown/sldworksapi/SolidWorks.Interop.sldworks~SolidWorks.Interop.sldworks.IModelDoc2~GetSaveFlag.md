---
title: "GetSaveFlag Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetSaveFlag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag.html"
---

# GetSaveFlag Method (IModelDoc2)

Gets whether the document is currently dirty and needs to be saved.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSaveFlag() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.GetSaveFlag()
```

### C#

```csharp
System.bool GetSaveFlag()
```

### C++/CLI

```cpp
System.bool GetSaveFlag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this document needs to be saved, false if not

## VBA Syntax

See [ModelDoc2::GetSaveFlag](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetSaveFlag.html).

## Examples

[Determine If Document Is Dirty (VBA)](Determine_if_Document_is_Dirty_Example_VB.htm)

## Remarks

This flag:

- determines if the Do you wish to save changes? dialog is displayed when the user tries to close the document. Many operations cause this flag to be set, and you can use [IModelDoc2::SetSaveFlag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetSaveFlag.html) to set this flag.
- is set to true if the document was created in an older version of SOLIDWORKS.
- is set to true for assemblies only when a subassembly has been saved. If this flag is set to true for a subassembly, then the assembly is not marked as dirty until the subassembly is saved.
- is reset to false after an end-user has saved the file.

NOTE: This method returns true if the model is opened read-only, the system option Don't prompt to save read-only referenced documents is not selected, and the model is dirty and visible.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveFlag.html)
[IConfiguration::IsDirty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDirty.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

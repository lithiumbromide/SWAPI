---
title: "SetSaveFlag Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetSaveFlag"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveFlag.html"
---

# SetSaveFlag Method (IModelDoc2)

Flags the document as dirty.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSaveFlag()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.SetSaveFlag()
```

### C#

```csharp
void SetSaveFlag()
```

### C++/CLI

```cpp
void SetSaveFlag();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::SetSaveFlag](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetSaveFlag.html).

## Examples

[Remove Textures from Assembly Components (VBA)](Remove_Textures_from_Assembly_Components_Example_VB.htm)

## Remarks

If the user tries to close the part, the Do you wish to save changes? dialog is displayed.

If SOLIDWORKS data has changed, this method marks the SOLIDWORKS document as dirty so that the end-user is prompted when attempting to close the document. You might want to use this method with applications that use [IModelDoc2::IGet3rdPartyStorage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGet3rdPartyStorage.html) to save stream data in SOLIDWORKS files.

If you have programmatically changed the SOLIDWORKS model, using this method is not necessary because the SOLIDWORKS document is flagged as dirty automatically.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetSaveFlag Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSaveFlag.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

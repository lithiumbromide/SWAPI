---
title: "HideComponent2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "HideComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2.html"
---

# HideComponent2 Method (IModelDoc2)

Hides the selected component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub HideComponent2()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.HideComponent2()
```

### C#

```csharp
void HideComponent2()
```

### C++/CLI

```cpp
void HideComponent2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::HideComponent2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~HideComponent2.html).

## Examples

[Undo Hidden Component and Fire Post-Notify Event (VB60](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)
[Undo Hidden Component and Fire Post-Notify Event (VB.NET)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)
[Undo Hidden Component and Fire Post-Notify Event (C#)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

## Remarks

This method is only available for [IDrawingDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc.html) and [IAssemblyDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc.html) objects; it is not available for [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html) objects.

To show a selected component, call [IModelDoc2::ShowComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowComponent2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ShowComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowComponent2.html)
[IModelDoc2::IsActive Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsActive.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

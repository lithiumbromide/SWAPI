---
title: "AutoSpaceComponentsOnDrag Property (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "AutoSpaceComponentsOnDrag"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~AutoSpaceComponentsOnDrag.html"
---

# AutoSpaceComponentsOnDrag Property (IExplodeStep)

Gets or sets whether to automatically space a group of components equally along an axis as you drag them.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoSpaceComponentsOnDrag As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Boolean

instance.AutoSpaceComponentsOnDrag = value

value = instance.AutoSpaceComponentsOnDrag
```

### C#

```csharp
System.bool AutoSpaceComponentsOnDrag {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoSpaceComponentsOnDrag {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to automatically space components equally along an axis as you drag them, false to not (see **Remarks**)

## VBA Syntax

See [ExplodeStep::AutoSpaceComponentsOnDrag](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~AutoSpaceComponentsOnDrag.html).

## Remarks

If this property is set to true, then, by default, [IExplodeStep::RotateAboutEachComponentOrigin](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotateAboutEachComponentOrigin.html) is false and [IExplodeStep::RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~RotationAngle.html) is 0.0.

If you set this property to false during editing of this step, then you must re-set the values for IExplodeStep::RotateAboutEachComponentOrigin and IExplodeStep::RotationAngle.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

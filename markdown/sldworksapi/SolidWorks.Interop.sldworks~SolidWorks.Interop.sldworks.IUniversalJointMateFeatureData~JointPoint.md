---
title: "JointPoint Property (IUniversalJointMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IUniversalJointMateFeatureData"
member: "JointPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.html"
---

# JointPoint Property (IUniversalJointMateFeatureData)

Gets or sets the joint point of this universal joint mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property JointPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IUniversalJointMateFeatureData
Dim value As System.Object

instance.JointPoint = value

value = instance.JointPoint
```

### C#

```csharp
System.object JointPoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ JointPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html) or [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)

## VBA Syntax

See [UniversalJointMateFeatureData::JointPoint](ms-its:sldworksapivb6.chm::/sldworks~UniversalJointMateFeatureData~JointPoint.html).

## Remarks

This property is valid only if [IUniversalJointMateFeatureData::DefineJointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint.html) is true.

## See Also

[IUniversalJointMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html)
[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

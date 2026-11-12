---
title: "DefineJointPoint Property (IUniversalJointMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IUniversalJointMateFeatureData"
member: "DefineJointPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint.html"
---

# DefineJointPoint Property (IUniversalJointMateFeatureData)

Gets or sets whether to define a joint point.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefineJointPoint As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IUniversalJointMateFeatureData
Dim value As System.Boolean

instance.DefineJointPoint = value

value = instance.DefineJointPoint
```

### C#

```csharp
System.bool DefineJointPoint {get; set;}
```

### C++/CLI

```cpp
property System.bool DefineJointPoint {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to define a joint point, false to not

## VBA Syntax

See [UniversalJointMateFeatureData::DefineJointPoint](ms-its:sldworksapivb6.chm::/sldworks~UniversalJointMateFeatureData~DefineJointPoint.html).

## Examples

See the [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html) example.

## Remarks

If this property is set to true, then specify [IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.html).

## See Also

[IUniversalJointMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html)
[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

---
title: "EntitiesToMate Property (IUniversalJointMateFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IUniversalJointMateFeatureData"
member: "EntitiesToMate"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~EntitiesToMate.html"
---

# EntitiesToMate Property (IUniversalJointMateFeatureData)

Gets or sets the entities to mate in this universal joint mate.

## Syntax

### Visual Basic (Declaration)

```vb
Property EntitiesToMate As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IUniversalJointMateFeatureData
Dim value As System.Object

instance.EntitiesToMate = value

value = instance.EntitiesToMate
```

### C#

```csharp
System.object EntitiesToMate {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EntitiesToMate {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of two entities to mate (see **Remarks**)

## VBA Syntax

See [UniversalJointMateFeatureData::EntitiesToMate](ms-its:sldworksapivb6.chm::/sldworks~UniversalJointMateFeatureData~EntitiesToMate.html).

## Examples

See the [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html) example.

## Remarks

Populate the array of this property with the cylindrical [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html) of two shaft components.

Instead of specifying this property, you can use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1. You can pre-select mate entities during mate creation, but not during mate editing.

## See Also

[IUniversalJointMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html)
[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0

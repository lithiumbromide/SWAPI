---
title: "Bodies Property (IDeleteBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteBodyFeatureData"
member: "Bodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~Bodies.html"
---

# Bodies Property (IDeleteBodyFeatureData)

Gets or sets the bodies to delete or keep.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteBodyFeatureData
Dim value As System.Object

instance.Bodies = value

value = instance.Bodies
```

### C#

```csharp
System.object Bodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to delete or keep

## VBA Syntax

See [DeleteBodyFeatureData::Bodies](ms-its:sldworksapivb6.chm::/sldworks~DeleteBodyFeatureData~Bodies.html).

## Remarks

Call [IDeleteBodyFeatureData::KeepBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteBodyFeatureData~KeepBodies.html) to specify whether to keep or delete the bodies.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)
[IDeleteBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html)
[IDeleteBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~GetBodiesCount.html)
[IDeleteBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~IGetBodies.html)
[IDeleteBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData~ISetBodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

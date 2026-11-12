---
title: "JoinedParts Property (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "JoinedParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~JoinedParts.html"
---

# JoinedParts Property (IJoinFeatureData)

Gets and sets the parts to join.

## Syntax

### Visual Basic (Declaration)

```vb
Property JoinedParts As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim value As System.Object

instance.JoinedParts = value

value = instance.JoinedParts
```

### C#

```csharp
System.object JoinedParts {get; set;}
```

### C++/CLI

```cpp
property System.Object^ JoinedParts {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of joined parts, the [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) objects

## VBA Syntax

See [JoinFeatureData::JoinedParts](ms-its:sldworksapivb6.chm::/sldworks~JoinFeatureData~JoinedParts.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)
[IJoinFeatureData::GetJoinedPartsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~GetJoinedPartsCount.html)
[IJoinFeatureData::IGetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~IGetJoinedParts.html)
[IJoinFeatureData::ISetJoinedParts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ISetJoinedParts.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

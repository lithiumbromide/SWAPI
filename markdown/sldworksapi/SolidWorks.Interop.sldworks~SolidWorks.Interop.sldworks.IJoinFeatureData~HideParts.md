---
title: "HideParts Property (IJoinFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJoinFeatureData"
member: "HideParts"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~HideParts.html"
---

# HideParts Property (IJoinFeatureData)

Gets or sets whether the original components are hidden after joined.

## Syntax

### Visual Basic (Declaration)

```vb
Property HideParts As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IJoinFeatureData
Dim value As System.Boolean

instance.HideParts = value

value = instance.HideParts
```

### C#

```csharp
System.bool HideParts {get; set;}
```

### C++/CLI

```cpp
property System.bool HideParts {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the original components are hidden after joined, false to not

## VBA Syntax

See [JoinFeatureData::HideParts](ms-its:sldworksapivb6.chm::/sldworks~JoinFeatureData~HideParts.html).

## See Also

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.html)
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

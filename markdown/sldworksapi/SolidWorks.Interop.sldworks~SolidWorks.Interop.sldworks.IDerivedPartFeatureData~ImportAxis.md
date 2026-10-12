---
title: "ImportAxis Property (IDerivedPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDerivedPartFeatureData"
member: "ImportAxis"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData~ImportAxis.html"
---

# ImportAxis Property (IDerivedPartFeatureData)

Gets or sets whether to import the axis with the derived part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImportAxis As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDerivedPartFeatureData
Dim value As System.Boolean

instance.ImportAxis = value

value = instance.ImportAxis
```

### C#

```csharp
System.bool ImportAxis {get; set;}
```

### C++/CLI

```cpp
property System.bool ImportAxis {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import its axis, false to not

## VBA Syntax

See [DerivedPartFeatureData::ImportAxis](ms-its:sldworksapivb6.chm::/sldworks~DerivedPartFeatureData~ImportAxis.html).

## See Also

[IDerivedPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData.html)
[IDerivedPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0

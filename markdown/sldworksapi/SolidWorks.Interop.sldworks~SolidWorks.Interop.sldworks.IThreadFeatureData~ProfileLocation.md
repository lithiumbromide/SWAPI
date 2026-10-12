---
title: "ProfileLocation Property (IThreadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IThreadFeatureData"
member: "ProfileLocation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ProfileLocation.html"
---

# ProfileLocation Property (IThreadFeatureData)

Gets or sets the point or vertex where to start the helix on the thread profile sketch of this thread feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileLocation As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IThreadFeatureData
Dim value As System.Object

instance.ProfileLocation = value

value = instance.ProfileLocation
```

### C#

```csharp
System.object ProfileLocation {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ProfileLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html) or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html) in the thread profile sketch where to start the thread helix

## VBA Syntax

See [ThreadFeatureData::ProfileLocation](ms-its:sldworksapivb6.chm::/sldworks~ThreadFeatureData~ProfileLocation.html).

## See Also

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.html)
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

---
title: "Profile Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "Profile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Profile.html"
---

# Profile Property (ISweepFeatureData)

Gets and sets the sketch profile or tool body for this sweep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Profile As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Object

instance.Profile = value

value = instance.Profile
```

### C#

```csharp
System.object Profile {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Profile {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Sketch profile or tool body for this sweep feature (see **Remarks**)

## VBA Syntax

See [SweepFeatureData::Profile](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~Profile.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

| If a... | Then the type of object is a... |
| --- | --- |
| Sketch profile | Face , edge , or curve |
| Tool body (see NOTE ) | Body that is convex, not merged with the main body and consists of one of the following: A revolved feature that consist of analytical geometry only, such as lines and arcs A cylindrical extruded feature |

**NOTE:** Tool bodies are supported in swept-cut features in SOLIDWORKS API 2017 FCS and later.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)
[ISweepFeatureData::CircularProfile Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~CircularProfile.html)
[ISweepFeatureData::GetProfileType Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetProfileType.html)
[ISweepFeatureData::Direction Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Direction.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

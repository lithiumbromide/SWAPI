---
title: "AssemblyFeatureScope Property (ISweepFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweepFeatureData"
member: "AssemblyFeatureScope"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AssemblyFeatureScope.html"
---

# AssemblyFeatureScope Property (ISweepFeatureData)

Gets and sets whether this swept-cut feature affects only selected components in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyFeatureScope As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISweepFeatureData
Dim value As System.Boolean

instance.AssemblyFeatureScope = value

value = instance.AssemblyFeatureScope
```

### C#

```csharp
System.bool AssemblyFeatureScope {get; set;}
```

### C++/CLI

```cpp
property System.bool AssemblyFeatureScope {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the swept-cutfeature affects only selected components in the assembly, false if affects all components in the assembly (**see Remarks**)

## VBA Syntax

See [SweepFeatureData::AssemblyFeatureScope](ms-its:sldworksapivb6.chm::/sldworks~SweepFeatureData~AssemblyFeatureScope.html).

## Examples

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html) examples.

## Remarks

Use this property, [ISweepFeatureData::AutoSelectComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISweepFeatureData~AutoSelectComponents.html), and [ISweepFeatureData::PropagateFeatureToParts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PropagateFeatureToParts.html) to insert sweep cuts into an assembly.

This API works with ISweepFeatureData::AutoSelectComponents to configure the scope of an assembly sweep feature. This API performs the same configuration that is done in the Feature Scope section of the PropertyManager page of the sweep feature:

| AssemblyFeatureScope setting | AutoSelectComponents setting | PropertyManager page Feature Scope setting |
| --- | --- | --- |
| False | Ignored | All components selected Auto-select not visible |
| True | If true, affected components are automatically selected If false, manually select the affected components before calling this API | Selected components selected If Auto-select is not checked, then manually select components |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.html)
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0

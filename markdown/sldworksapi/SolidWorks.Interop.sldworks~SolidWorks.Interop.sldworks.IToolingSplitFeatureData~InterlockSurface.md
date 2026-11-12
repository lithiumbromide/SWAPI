---
title: "InterlockSurface Property (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "InterlockSurface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~InterlockSurface.html"
---

# InterlockSurface Property (IToolingSplitFeatureData)

Gets or sets whether to create an interlock surface for this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property InterlockSurface As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim value As System.Boolean

instance.InterlockSurface = value

value = instance.InterlockSurface
```

### C#

```csharp
System.bool InterlockSurface {get; set;}
```

### C++/CLI

```cpp
property System.bool InterlockSurface {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create an interlock surface, false to not

## VBA Syntax

See [ToolingSplitFeatureData::InterlockSurface](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~InterlockSurface.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

If this property is set to true, then you can specify a [draft angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IToolingSplitFeatureData~Angle.html) for the interlock surface.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

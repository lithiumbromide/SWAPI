---
title: "Depth Property (IToolingSplitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IToolingSplitFeatureData"
member: "Depth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData~Depth.html"
---

# Depth Property (IToolingSplitFeatureData)

Gets or sets the depth of the block in the specified direction for this tooling split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Depth( _
   ByVal Dir As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IToolingSplitFeatureData
Dim Dir As System.Integer
Dim value As System.Double

instance.Depth(Dir) = value

value = instance.Depth(Dir)
```

### C#

```csharp
System.double Depth(
   System.int Dir
) {get; set;}
```

### C++/CLI

```cpp
property System.double Depth {
   System.double get(System.int Dir);
   void set (System.int Dir, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Dir`: - 0 = Depth in Direction 1
  - 1 = Depth in Direction 2

### Property Value

Depth

## VBA Syntax

See [ToolingSplitFeatureData::Depth](ms-its:sldworksapivb6.chm::/sldworks~ToolingSplitFeatureData~Depth.html).

## Examples

See the [IToolingSplitFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IToolingSplitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData.html)
[IToolingSplitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0

---
title: "CustomizeCallout Property (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "CustomizeCallout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~CustomizeCallout.html"
---

# CustomizeCallout Property (IAdvancedHoleFeatureData)

Gets or sets whether to customize the hole callouts of the elements of this Advanced Hole.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomizeCallout As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleFeatureData
Dim value As System.Boolean

instance.CustomizeCallout = value

value = instance.CustomizeCallout
```

### C#

```csharp
System.bool CustomizeCallout {get; set;}
```

### C++/CLI

```cpp
property System.bool CustomizeCallout {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to customize hole callouts, false to use default hole callouts

## VBA Syntax

See [AdvancedHoleFeatureData::CustomizeCallout](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~CustomizeCallout.html).

## Examples

See the [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html) examples.

## Remarks

If you set this property to true, use [IAdvancedHoleElementData::CalloutString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.html) to customize the hole callouts.

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

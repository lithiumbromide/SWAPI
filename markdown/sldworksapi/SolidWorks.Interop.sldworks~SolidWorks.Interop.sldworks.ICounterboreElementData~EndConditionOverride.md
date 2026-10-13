---
title: "EndConditionOverride Property (ICounterboreElementData)"
project: "SOLIDWORKS API Help"
interface: "ICounterboreElementData"
member: "EndConditionOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData~EndConditionOverride.html"
---

# EndConditionOverride Property (ICounterboreElementData)

Gets or sets whether to override the end condition of this counterbore hole element.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndConditionOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICounterboreElementData
Dim value As System.Boolean

instance.EndConditionOverride = value

value = instance.EndConditionOverride
```

### C#

```csharp
System.bool EndConditionOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool EndConditionOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override the end condition, false to not (see **Remarks**)

## VBA Syntax

See [CounterboreElementData::EndConditionOverride](ms-its:sldworksapivb6.chm::/sldworks~CounterboreElementData~EndConditionOverride.html).

## Examples

See the [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.html) examples.

## Remarks

This property can be set only if [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.html) is set to false.

Set this property to true and specify [IAdvancedHoleElementData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~EndCondition.html) to override the end condition.

## See Also

[ICounterboreElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.html)
[ICounterboreElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0

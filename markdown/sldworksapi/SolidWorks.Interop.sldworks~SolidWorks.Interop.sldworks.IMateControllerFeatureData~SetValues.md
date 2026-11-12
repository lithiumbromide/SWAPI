---
title: "SetValues Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "SetValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~SetValues.html"
---

# SetValues Method (IMateControllerFeatureData)

Sets the mate values for the specified mate position.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetValues( _
   ByVal PositionName As System.String, _
   ByVal Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim Values As System.Object

instance.SetValues(PositionName, Values)
```

### C#

```csharp
void SetValues(
   System.string PositionName,
   System.object Values
)
```

### C++/CLI

```cpp
void SetValues(
   System.String^ PositionName,
   System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionName`: Name of mate position
- `Values`: Array of values for all mates in PositionName

## VBA Syntax

See [MateControllerFeatureData::SetValues](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~SetValues.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## Remarks

The number of items in Values must correspond to the number of mates passed to [IMateControllerFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.html) or the number of pre-selected mates.

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

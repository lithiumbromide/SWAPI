---
title: "ReOrderPositions Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "ReOrderPositions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~ReOrderPositions.html"
---

# ReOrderPositions Method (IMateControllerFeatureData)

Reorders the mate positions in this mate controller.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReOrderPositions( _
   ByVal Positions As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim Positions As System.Object

instance.ReOrderPositions(Positions)
```

### C#

```csharp
void ReOrderPositions(
   System.object Positions
)
```

### C++/CLI

```cpp
void ReOrderPositions(
   System.Object^ Positions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Positions`: Array of re-ordered mate positions

## VBA Syntax

See [MateControllerFeatureData::ReOrderPositions](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~ReOrderPositions.html).

## Remarks

Before calling this method, use [IMateControllerFeatureData::GetPositions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~GetPositions.html) to get the existing mate positions.

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

---
title: "DeletePosition Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "DeletePosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~DeletePosition.html"
---

# DeletePosition Method (IMateControllerFeatureData)

Deletes the specified mate position from this mate controller.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeletePosition( _
   ByVal PositionName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim value As System.Boolean

value = instance.DeletePosition(PositionName)
```

### C#

```csharp
System.bool DeletePosition(
   System.string PositionName
)
```

### C++/CLI

```cpp
System.bool DeletePosition(
   System.String^ PositionName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionName`: Name of mate position to delete

### Return Value

True if mate position successfully deleted, false if not

## VBA Syntax

See [MateControllerFeatureData::DeletePosition](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~DeletePosition.html).

## Remarks

Before calling this method, use [IMateControllerFeatureData::GetPositions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~GetPositions.html) to get the existing mate positions.

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

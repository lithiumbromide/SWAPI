---
title: "AddNewPosition Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "AddNewPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AddNewPosition.html"
---

# AddNewPosition Method (IMateControllerFeatureData)

Adds a mate position name to this mate controller.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddNewPosition( _
   ByVal PositionName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim value As System.Boolean

value = instance.AddNewPosition(PositionName)
```

### C#

```csharp
System.bool AddNewPosition(
   System.string PositionName
)
```

### C++/CLI

```cpp
System.bool AddNewPosition(
   System.String^ PositionName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionName`: Name of mate position to add

### Return Value

True if mate position successfully created, false if not

## VBA Syntax

See [MateControllerFeatureData::AddNewPosition](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~AddNewPosition.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

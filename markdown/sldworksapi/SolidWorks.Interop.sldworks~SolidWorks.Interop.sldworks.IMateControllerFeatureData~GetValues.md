---
title: "GetValues Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "GetValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~GetValues.html"
---

# GetValues Method (IMateControllerFeatureData)

Gets the mate values for the specified mate position.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetValues( _
   ByVal PositionName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim value As System.Object

value = instance.GetValues(PositionName)
```

### C#

```csharp
System.object GetValues(
   System.string PositionName
)
```

### C++/CLI

```cpp
System.Object^ GetValues(
   System.String^ PositionName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionName`: Name of mate position

### Return Value

Array of values for all mates in PositionName

## VBA Syntax

See [MateControllerFeatureData::GetValues](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~GetValues.html).

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

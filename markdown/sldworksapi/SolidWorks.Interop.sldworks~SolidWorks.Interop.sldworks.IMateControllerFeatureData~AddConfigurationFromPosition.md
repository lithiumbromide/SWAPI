---
title: "AddConfigurationFromPosition Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "AddConfigurationFromPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AddConfigurationFromPosition.html"
---

# AddConfigurationFromPosition Method (IMateControllerFeatureData)

Adds a configuration from the specified mate position.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddConfigurationFromPosition( _
   ByVal PositionName As System.String, _
   ByVal IsUpdate As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim PositionName As System.String
Dim IsUpdate As System.Boolean
Dim value As System.Boolean

value = instance.AddConfigurationFromPosition(PositionName, IsUpdate)
```

### C#

```csharp
System.bool AddConfigurationFromPosition(
   System.string PositionName,
   System.bool IsUpdate
)
```

### C++/CLI

```cpp
System.bool AddConfigurationFromPosition(
   System.String^ PositionName,
   System.bool IsUpdate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PositionName`: Name of mate position
- `IsUpdate`: True if an update, false if not

### Return Value

True if configuration successfully added, false if not

## VBA Syntax

See [MateControllerFeatureData::AddConfigurationFromPosition](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~AddConfigurationFromPosition.html).

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31

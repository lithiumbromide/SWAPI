---
title: "GetDouble Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetDouble"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetDouble.html"
---

# GetDouble Method (ISafeArrayUtility)

Gets the specified double value in a Variant SafeArray of double values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDouble( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetDouble(VariantArray, Index)
```

### C#

```csharp
System.double GetDouble(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetDouble(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of double values
- `Index`: Index of double value

### Return Value

Double value

## Examples

[Get Spline Points (C++)](Get_Spline_Points_Example_CPlusPlus_COM.htm)

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutDouble Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutDouble.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

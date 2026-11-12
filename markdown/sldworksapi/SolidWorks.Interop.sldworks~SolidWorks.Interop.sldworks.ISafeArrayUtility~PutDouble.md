---
title: "PutDouble Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutDouble"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutDouble.html"
---

# PutDouble Method (ISafeArrayUtility)

Adds the specified double value to a Variant SafeArray of double values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutDouble( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Double

instance.PutDouble(VariantArray, Index, Value)
```

### C#

```csharp
void PutDouble(
   out System.object VariantArray,
   System.int Index,
   System.double Value
)
```

### C++/CLI

```cpp
void PutDouble(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of double values
- `Index`: Index of double value
- `Value`: Double value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetDouble Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetDouble.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

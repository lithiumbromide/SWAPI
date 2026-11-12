---
title: "PutBoolean Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutBoolean"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBoolean.html"
---

# PutBoolean Method (ISafeArrayUtility)

Adds the specified Boolean value to a Variant SafeArray of Boolean values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutBoolean( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Boolean

instance.PutBoolean(VariantArray, Index, Value)
```

### C#

```csharp
void PutBoolean(
   out System.object VariantArray,
   System.int Index,
   System.bool Value
)
```

### C++/CLI

```cpp
void PutBoolean(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.bool Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of Boolean values
- `Index`: Index of Boolean value
- `Value`: Boolean value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetBoolean Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBoolean.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

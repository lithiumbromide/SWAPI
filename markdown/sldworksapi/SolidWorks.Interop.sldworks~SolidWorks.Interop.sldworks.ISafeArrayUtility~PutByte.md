---
title: "PutByte Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "PutByte"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutByte.html"
---

# PutByte Method (ISafeArrayUtility)

Adds the specified byte value to a Variant SafeArray of byte values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PutByte( _
   ByRef VariantArray As System.Object, _
   ByVal Index As System.Integer, _
   ByVal Value As System.Byte _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim Value As System.Byte

instance.PutByte(VariantArray, Index, Value)
```

### C#

```csharp
void PutByte(
   out System.object VariantArray,
   System.int Index,
   System.byte Value
)
```

### C++/CLI

```cpp
void PutByte(
   [Out] System.Object^ VariantArray,
   System.int Index,
   System.byte Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of byte values
- `Index`: Index of byte value
- `Value`: Byte value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::GetByte Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetByte.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

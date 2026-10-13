---
title: "GetByte Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetByte"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetByte.html"
---

# GetByte Method (ISafeArrayUtility)

Gets the specified byte value in a Variant SafeArray of byte values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetByte( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Byte
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Byte

value = instance.GetByte(VariantArray, Index)
```

### C#

```csharp
System.byte GetByte(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.byte GetByte(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of byte values
- `Index`: Index of byte value

### Return Value

Byte value

## Examples

[Get Object's Persistent Reference ID (C++)](Get_Object_s_Persistent_Reference_ID_Example_CPlusPlus_COM.htm)

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutByte Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutByte.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

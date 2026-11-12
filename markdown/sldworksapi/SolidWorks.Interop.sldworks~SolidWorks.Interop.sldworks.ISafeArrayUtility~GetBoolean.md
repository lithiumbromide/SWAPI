---
title: "GetBoolean Method (ISafeArrayUtility)"
project: "SOLIDWORKS API Help"
interface: "ISafeArrayUtility"
member: "GetBoolean"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~GetBoolean.html"
---

# GetBoolean Method (ISafeArrayUtility)

Gets the specified Boolean value in a Variant SafeArray of Boolean values.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBoolean( _
   ByVal VariantArray As System.Object, _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISafeArrayUtility
Dim VariantArray As System.Object
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.GetBoolean(VariantArray, Index)
```

### C#

```csharp
System.bool GetBoolean(
   System.object VariantArray,
   System.int Index
)
```

### C++/CLI

```cpp
System.bool GetBoolean(
   System.Object^ VariantArray,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VariantArray`: Variant SafeArray of Boolean values
- `Index`: Index of Boolean value

### Return Value

Boolean value

## See Also

[ISafeArrayUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility.html)
[ISafeArrayUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html)
[ISafeArrayUtility::PutBoolean Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility~PutBoolean.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0

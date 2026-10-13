---
title: "GetIgesErrorCode Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetIgesErrorCode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCode.html"
---

# GetIgesErrorCode Method (IBody2)

Gets the current IGES error code.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIgesErrorCode( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetIgesErrorCode(Index)
```

### C#

```csharp
System.int GetIgesErrorCode(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetIgesErrorCode(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Position of the error within the current list of errors

### Return Value

IGES error code

## VBA Syntax

See [Body2::GetIgesErrorCode](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetIgesErrorCode.html).

## Remarks

This method is intended for use during IGES processing only.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetIgesErrorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetIgesErrorCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0

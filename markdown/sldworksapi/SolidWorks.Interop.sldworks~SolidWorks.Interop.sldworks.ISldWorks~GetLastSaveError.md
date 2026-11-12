---
title: "GetLastSaveError Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetLastSaveError"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastSaveError.html"
---

# GetLastSaveError Method (ISldWorks)

Gets the last save error issued by Microsoft in the current session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLastSaveError( _
   ByRef FilePath As System.Object, _
   ByRef ErrorCode As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FilePath As System.Object
Dim ErrorCode As System.Object
Dim value As System.Object

value = instance.GetLastSaveError(FilePath, ErrorCode)
```

### C#

```csharp
System.object GetLastSaveError(
   out System.object FilePath,
   out System.object ErrorCode
)
```

### C++/CLI

```cpp
System.Object^ GetLastSaveError(
   [Out] System.Object^ FilePath,
   [Out] System.Object^ ErrorCode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`: Path name of the document causing the save error
- `ErrorCode`: Error code of the save

### Return Value

Text message of the save error

## VBA Syntax

See [SldWorks::GetLastSaveError](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetLastSaveError.html).

## Examples

[Get Last Save Error (VBA)](Get_Last_Save_Error_Example_VB.htm)
[Get Last Save Error (VB.NET)](Get_Last_Save_Error_Example_VBNET.htm)
[Get Last Save Error (C#)](Get_Last_Save_Error_Example_CSharp.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetErrorMessages Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetErrorMessages.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0

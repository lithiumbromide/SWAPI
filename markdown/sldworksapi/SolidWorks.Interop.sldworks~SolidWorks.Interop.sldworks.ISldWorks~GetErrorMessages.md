---
title: "GetErrorMessages Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetErrorMessages"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetErrorMessages.html"
---

# GetErrorMessages Method (ISldWorks)

Gets the last 20 messages issued in the current SOLIDWORKS Design session.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetErrorMessages( _
   ByRef Msgs As System.Object, _
   ByRef MsgIDs As System.Object, _
   ByRef MsgTypes As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Msgs As System.Object
Dim MsgIDs As System.Object
Dim MsgTypes As System.Object
Dim value As System.Integer

value = instance.GetErrorMessages(Msgs, MsgIDs, MsgTypes)
```

### C#

```csharp
System.int GetErrorMessages(
   out System.object Msgs,
   out System.object MsgIDs,
   out System.object MsgTypes
)
```

### C++/CLI

```cpp
System.int GetErrorMessages(
   [Out] System.Object^ Msgs,
   [Out] System.Object^ MsgIDs,
   [Out] System.Object^ MsgTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Msgs`: Array of the last 20 messages issued in this SOLIDWORKS Design session
- `MsgIDs`: Array of the resource IDs of the last 20 messages issued in this SOLIDWORKS Design
  session
- `MsgTypes`: Array of the types of the last 20 messages issued in this SOLIDWORKS Design
  session (see **Remarks**)

### Return Value

Number of messages issued in this SOLIDWORKS Design session

**NOTE:** The stack is cleared after calling this method.

## VBA Syntax

See [SldWorks::GetErrorMessages](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetErrorMessages.html).

## Examples

[Get Messages (VBA)](Get_Messages_Example_VB.htm)

## Remarks

The elements of the MsgTypes array are bitmasks of the Microsoft message-box system constants.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetLastSaveError Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLastSaveError.html)

## Availability

SOLIDWORKS 2006 SP1, Revision Number 14.1

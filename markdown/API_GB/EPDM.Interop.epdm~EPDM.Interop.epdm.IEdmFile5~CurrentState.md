---
title: "CurrentState Property (IEdmFile5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFile5"
member: "CurrentState"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~CurrentState.html"
---

# CurrentState Property (IEdmFile5)

Gets the file's current workflow state.

## Syntax

### Visual Basic

```vb
ReadOnly Property CurrentState As IEdmState5
```

### C#

```csharp
IEdmState5 CurrentState {get;}
```

### C++/CLI

```cpp
property IEdmState5^ CurrentState {
   IEdmState5^ get();
}
```

### Property Value

Current [workflow state](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html) of the file

## Examples

[Get File's State Transitions (C#)](Get_Files_State_Transitions_Example_CSharp.htm)
[Get File's State Transitions (VB.NET)](Get_Files_State_Transitions_Example_VBNET.htm)

## See Also

[IEdmFile5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html)
[IEdmFile5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5_members.html)

## Availability

SOLIDWORKS PDM Professional Version 5.2

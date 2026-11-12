---
title: "IEdmState5 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmState5"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5.html"
---

# IEdmState5 Interface

Allows you to access a workflow state.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmState5
   Inherits IEdmObject5
```

### C#

```csharp
public interface IEdmState5 : IEdmObject5
```

### C++/CLI

```cpp
public interface class IEdmState5 : public IEdmObject5
```

## Examples

[Get File's State Transitions (C#)](Get_Files_State_Transitions_Example_CSharp.htm)
[Get File's State Transitions (VB.NET)](Get_Files_State_Transitions_Example_VBNET.htm)

## Remarks

This interface:

- inherits from [IEdmObject5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html).
- is extended by [IEdmState6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState6.html).

## Accessors

[IEdmFile5::CurrentState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5~CurrentState.html)

[IEdmTransition5::FromState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5~FromState.html)

[IEdmTransition5::ToState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5~ToState.html)

[IEdmVault5::GetObject](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5~GetObject.html)

[IEdmWorkflow5::GetNextState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetNextState.html)

[IEdmWorkflow5::GetState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~GetState.html)

[IEdmWorkflow5::InitialState](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmWorkflow5~InitialState.html)

## See Also

[IEdmState5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmState5_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
[IEdmTransition5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmTransition5.html)

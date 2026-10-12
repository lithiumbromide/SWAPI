---
title: "EdmRect Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmRect"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html"
---

# EdmRect Structure

Encapsulates a rectangle and is identical to the Win32 RECT struct.

## Syntax

### Visual Basic

```vb
Public Structure EdmRect
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmRect : System.ValueType
```

### C++/CLI

```cpp
public value class EdmRect : public System.ValueType
```

## Examples

struct EdmRect{
integer [mlLeft](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect~mlLeft.html);
integer [mlTop](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect~mlTop.html);
integer [mlRight](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect~mlRight.html);
integer [mlBottom](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect~mlBottom.html);
};

## Examples

[Graph a Workflow (VB.NET)](Graph_Workflow_Example_VBNET.htm)
[Graph a Workflow (C#)](Graph_Workflow_Example_CSharp.htm)

## See Also

[EdmRect Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional

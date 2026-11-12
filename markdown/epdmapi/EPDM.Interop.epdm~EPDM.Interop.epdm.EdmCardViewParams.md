---
title: "EdmCardViewParams Structure"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmCardViewParams"
member: ""
kind: "topic"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams.html"
---

# EdmCardViewParams Structure

Contains card view parameters.

## Syntax

### Visual Basic

```vb
Public Structure EdmCardViewParams
   Inherits System.ValueType
```

### C#

```csharp
public struct EdmCardViewParams : System.ValueType
```

### C++/CLI

```cpp
public value class EdmCardViewParams : public System.ValueType
```

## Examples

struct EdmCardViewParams{
integer [mlFileID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlFileID.html);
integer [mlFolderID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlFolderID.html);
integer [mlCardID](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlCardID.html);
integer [mlX](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlX.html);
integer [mlY](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlY.html);
integer [mhParentWindow](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mhParentWindow.html);
integer [mlEdmCardViewFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams~mlEdmCardViewFlags.html);
};

## Examples

[Create Custom Card View (VB.NET)](Create_Custom_Card_View_Example_VBNET.htm)
[Create Custom Card View (C#)](Create_Custom_Card_View_Example_CSharp.htm)

## Remarks

Used by [IEdmVault10::CreateCardViewEx2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault10~CreateCardViewEx2.html) to create a card view.

## See Also

[EdmCardViewParams Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardViewParams_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)

## Availability

SOLIDWORKS PDM Professional 2009

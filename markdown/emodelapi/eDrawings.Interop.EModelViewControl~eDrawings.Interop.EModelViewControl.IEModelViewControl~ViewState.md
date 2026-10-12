---
title: "ViewState Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ViewState"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ViewState.html"
---

# ViewState Property (IEModelViewControl)

Gets or sets the view state.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewState( _
   ByVal state As EMVViewState _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim state As EMVViewState
Dim value As System.Boolean

instance.ViewState(state) = value

value = instance.ViewState(state)
```

### C#

```csharp
System.bool ViewState(
   EMVViewState state
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewState {
   System.bool get(EMVViewState state);
   void set (EMVViewState state, System.bool value);
}
```

### Parameters

- `state`: View state as defined by [EMVViewState](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVViewState.html)

### Property Value

True if the view state is set, false if not

## VBA Syntax

See [EModelViewControl::ViewState](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ViewState.html).

## Examples

```vb
MyEModelViewControl.ViewState(eMVPerspective) = True 'Sets view state to perspective or true
MyEModelViewControl.ViewState(eMVPerspective) ' Gets view state
See IEModelViewControl examples.
```

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ShowShadedEdges Property ()](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ShowShadedEdges.html)

## Availability

eDrawings API 2005 SP0

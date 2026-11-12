---
title: "ViewState Property (IEModelMarkupControl)"
project: "eDrawings API Help"
interface: "IEModelMarkupControl"
member: "ViewState"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl~ViewState.html"
---

# ViewState Property (IEModelMarkupControl)

Gets or sets the view state.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewState( _
   ByVal state As EMVMarkupViewState _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelMarkupControl
Dim state As EMVMarkupViewState
Dim value As System.Boolean

instance.ViewState(state) = value

value = instance.ViewState(state)
```

### C#

```csharp
System.bool ViewState(
   EMVMarkupViewState state
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewState {
   System.bool get(EMVMarkupViewState state);
   void set (EMVMarkupViewState state, System.bool value);
}
```

### Parameters

- `state`: View states as defined in [EMVMarkupViewState](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.EMVMarkupViewState.html)

### Property Value

True if the view state is set, false to not

## VBA Syntax

See [EModelMarkupControl::ViewState](ms-its:emodelapivb6.chm::/EModelViewMarkup~EModelMarkupControl~ViewState.html).

## See Also

[IEModelMarkupControl Interface](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html)
[IEModelMarkupControl Members](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl_members.html)

## Availability

eDrawings API 2005 SP0

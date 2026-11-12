---
title: "ComponentState Property (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "ComponentState"
kind: "property"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentState.html"
---

# ComponentState Property (IEModelViewControl)

Gets or sets the state of the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentState( _
   ByVal Name As System.String, _
   ByVal state As EMVComponentState _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim Name As System.String
Dim state As EMVComponentState
Dim value As System.Boolean

instance.ComponentState(Name, state) = value

value = instance.ComponentState(Name, state)
```

### C#

```csharp
System.bool ComponentState(
   System.string Name,
   EMVComponentState state
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ComponentState {
   System.bool get(System.String^ Name, EMVComponentState state);
   void set (System.String^ Name, EMVComponentState state, System.bool value);
}
```

### Parameters

- `Name`: Name of the component
- `state`: State of the component as defined in [EMVComponentState](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.EMVComponentState.html)

### Property Value

True if the state of the component is set, false if not

## VBA Syntax

See [EModelViewControl::ComponentState](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~ComponentState.html).

## Remarks

Before calling this property, call [IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html) to get a valid value for Name.

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)
[IEModelViewControl::ComponentCount](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentCount.html)
[IEModelViewControl::ComponentConfigurationName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentConfigurationName.html)
[IEModelViewControl::ComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentName.html)
[IEModelViewControl::ComponentTransform](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~ComponentTransform.html)
[IEModelViewControl::GetSelectedComponentName](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~GetSelectedComponentName.html)

## Availability

eDrawings API 2005 SP0

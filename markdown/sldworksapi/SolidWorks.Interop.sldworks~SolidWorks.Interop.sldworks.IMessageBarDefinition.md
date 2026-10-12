---
title: "IMessageBarDefinition Interface"
project: "SOLIDWORKS API Help"
interface: "IMessageBarDefinition"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition.html"
---

# IMessageBarDefinition Interface

Allows access to a message bar in an add-in.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMessageBarDefinition
```

### Visual Basic (Usage)

```vb
Dim instance As IMessageBarDefinition
```

### C#

```csharp
public interface IMessageBarDefinition
```

### C++/CLI

```cpp
public interface class IMessageBarDefinition
```

## VBA Syntax

See [MessageBarDefinition](ms-its:sldworksapivb6.chm::/sldworks~MessageBarDefinition.html).

## Examples

See the [IMessageBarHandler](ms-its:swpublishedapi.chm::/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html) examples.

## Remarks

A message bar:

- Allows an add-in to display a message to users.
- Is a modeless dialog that contains a unique message.
- Only appears within the context of a document open in its own frame.
- May be stacked with other message bars in the user interface.
- Requires an IMessageBarHandler to handle message bar events.

## Accessors

[ISldWorks::DefineMessageBar](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineMessageBar.html)

## Access Diagram

[MessageBarDefinition](SWObjectModel.pdf#MessageBarDefinition)

## See Also

[IMessageBarDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMessageBarDefinition_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IUserNotificationDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserNotificationDefinition.html)

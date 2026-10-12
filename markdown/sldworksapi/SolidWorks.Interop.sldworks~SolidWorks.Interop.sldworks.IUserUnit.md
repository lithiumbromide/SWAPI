---
title: "IUserUnit Interface"
project: "SOLIDWORKS API Help"
interface: "IUserUnit"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.html"
---

# IUserUnit Interface

Allows you to manage units.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IUserUnit
```

### Visual Basic (Usage)

```vb
Dim instance As IUserUnit
```

### C#

```csharp
public interface IUserUnit
```

### C++/CLI

```cpp
public interface class IUserUnit
```

## VBA Syntax

See [UserUnit](ms-its:sldworksapivb6.chm::/sldworks~UserUnit.html).

## Examples

[Get and Set Document Units (VBA)](Get_and_Set_User_Units_Example_VB.htm)
[Get and Set Document Units (VB.NET)](Get_and_Set_User_Units_Example_VBNET.htm)
[Get and Set Document Units (C#)](Get_and_Set_User_Units_Example_CSharp.htm)

## Remarks

| If you obtain IUserUnit using... | Then IUserUnit's properties are... |
| --- | --- |
| IModelDoc2 | Read only and persistent. Use IModelDocExtension::SetUserPreference* methods to set the units properties of a document. |
| ISldWorks | Read-write, but not persistent. The instance of IUserUnit returned by ISldWorks is empty and not tied to any document. Use this instance as a template to store units properties at runtime. |

**NOTE**: Use this interface instead of **mo_UserUnits.h** file in `public_documents`**\appcomm** of your SOLIDWORKS installation. If you previously used **mo_UserUnits.h**, you should change your applications to use this interface.

## Accessors

[IModelDoc2::GetUserUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUserUnit.html) and [IModelDoc2::IGetUserUnit](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetUserUnit.html)

[ISldWorks::GetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit.html) and [ISldWorks::IGetUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetUserUnit.html)

## Access Diagram

[UserUnit](SWObjectModel.pdf#UserUnit)

## See Also

[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

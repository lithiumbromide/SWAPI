---
title: "Interface Pointers"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Interface_Pointers.htm"
---

# Interface Pointers

Interface pointers can be an area of confusion with unmanaged C++ programming. Each SOLIDWORKS API method that returns an interface pointer automatically increments the reference count on the interface pointer by 1.

- COM implementations. You can call a SOLIDWORKS API that returns an interface pointer. You can then use this pointer as you like, but you are responsible for releasing it.

This unmanaged C++ COM example demonstrates how to handle interface pointers.

```vb
{
```

```vb
 LPMODELDOC2 m_ModelDoc = NULL;
// Get the IModelDoc pointer
 HRESULT res = UserApp->getSWApp()->get_IActiveDoc( &m_ModelDoc );

 if( m_ModelDoc == NULL )
 return;

 LPPARTDOC m_PartDoc = NULL;

// Get the IPartDoc pointer
 res = m_ModelDoc->QueryInterface(IID_IPartDoc, (LPVOID *)&m_PartDoc);
 ASSERT( res == S_OK );
.
.
// Use the interface pointers within your code and then release them when done
.
.
 m_ModelDoc->Release(); // Release the IModelDoc2 pointer
 m_PartDoc->Release(); // Release the IPartDoc pointer
```

```vb
 }
```

NOTE: LPINTERFACE is a typedef and a pointer to the named interface. e.g., LPPARTDOC points to the PartDoc interface, LPMODELDOC2 points to the ModelDoc2 interface, etc.

You can also use [smart pointers](Smart_Pointers.htm) with COM implementations. CComPtr is an ATL smart pointer. IInterfacePtr (e.g., IModelDoc2Ptr) is also a smart pointer that does many of the same things as CComPtr, but it is not part of ATL. It is a typedef that resolves to a _com_ptr_t (defined in comip.h) using _COM_SMARTPTR_TYPEDEF. For more information about using smart pointers with container classes, see [STL Container Classes and Smart Pointers](STL_Container_Classes_and_Smart_Pointers.htm).

For an example of using smart pointers, see [Access Assembly Example (C++ COM)](sldworksAPI.chm::/Access_Assembly_Example_CPlusPlus_COM.htm).

- Dispatch implementations. The release of the interface pointer is hidden in the destructor of the Dispatch objects (for example, IModelDoc2, IFace2, and so on). This implies that attaching an interface pointer to more than one of these Dispatch objects will cause a release to be performed by each of the objects as they go out of scope. This will cause a problem because the reference count was only incremented once when the interface pointer was returned to you.

To avoid this problem, you must manually increment the reference count ( pdisp->AddRef(); ) if you are attaching the interface pointer to more than one object.

This C++ Dispatch example demonstrates how to handle the reference count on interface pointers.

```vb
{
```

```vb
LPDISPATCH modDisp;
 // Get interface pointer to the active document
 modDisp = UserApp->getSWApp()->GetActiveDoc();
// Reference count on modDisp automatically incremented by 1

if( modDisp == NULL )
 return;

// Attach to the IModelDoc2 object
 IModelDoc2 m_ModelDoc( modDisp );

// Attach to the IPartDoc object
 IPartDoc m_PartDoc( modDisp );

 // Manually increment the reference count on modDisp because
// you use modDisp a second time
modDisp->AddRef();
.
.
// Use objects within your code
.
.

// Variables go out of scope and destructors are called for IModelDoc2 and IPartDoc,
// which decrements the reference count on modDisp by two
```

```vb
}
```

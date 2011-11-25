vaods9 API
==========

.. admonition:: Exercise (for the interested reader): Special methods and properties

  Wait. Didn't we just set ``pl.ref`` to be an float?  How can ``pl.ref`` be an
    float and a ``Parameter`` object?

.. raw:: html

   <p class="flip0">Click to Show/Hide Solution</p> <div class="panel0">

   The answer is that pl.ref is in fact an object, but its model class supports a
   special setter method ``__setattr__()`` that updates the pl.ref.val attribute
   underneath.  The ``property`` function defines custom getter and setter
   functions for a particular class attribute::

     class Parameter(object):
           def __init__(self):
                     # private attribute intended to be reference as 'val'.
                               self._value = 1.0

                                     def _get_val(self): return self._value
                                           def _set_val(self, value): self._value = value
                                                 # setup a 'val' attribute
                                                       val = property(_get_val, _set_val)

.. raw:: html

   </div>


.. automodule:: vaods9
   :members:
   :undoc-members:
.. :inherited-members:

# Copyright (c) 2014 Cisco Systems, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from nova import test
from nova_solverscheduler.scheduler.solvers.constraints \
        import affinity_constraint
from nova_solverscheduler.tests.scheduler import solver_scheduler_fakes \
        as fakes


class TestSameHostConstraint(test.NoDBTestCase):

    def setUp(self):
        super(TestSameHostConstraint, self).setUp()
        self.constraint_cls = affinity_constraint.SameHostConstraint
        self._generate_fake_constraint_input()

    def _generate_fake_constraint_input(self):
        self.fake_filter_properties = {
                'instance_uuids': ['fake_uuid_%s' % x for x in range(3)],
                'num_instances': 3}
        host1 = fakes.FakeSolverSchedulerHostState('host1', 'node1', {})
        host2 = fakes.FakeSolverSchedulerHostState('host2', 'node1', {})
        self.fake_hosts = [host1, host2]

    @mock.patch('nova_solverscheduler.scheduler.solvers.constraints.'
                'affinity_constraint.SameHostConstraint.'
                'host_filter_cls')
    def test_get_constraint_matrix(self, mock_filter_cls):
        expected_cons_mat = [
            [True, True, True],
            [False, False, False]]
        mock_filter = mock_filter_cls.return_value
        mock_filter.host_passes.side_effect = [True, False]
        cons_mat = self.constraint_cls().get_constraint_matrix(
                    self.fake_hosts, self.fake_filter_properties)
        self.assertEqual(expected_cons_mat, cons_mat)


class TestDifferentHostConstraint(test.NoDBTestCase):

    def setUp(self):
        super(TestDifferentHostConstraint, self).setUp()
        self.constraint_cls = affinity_constraint.DifferentHostConstraint
        self._generate_fake_constraint_input()

    def _generate_fake_constraint_input(self):
        self.fake_filter_properties = {
                'instance_uuids': ['fake_uuid_%s' % x for x in range(3)],
                'num_instances': 3}
        host1 = fakes.FakeSolverSchedulerHostState('host1', 'node1', {})
        host2 = fakes.FakeSolverSchedulerHostState('host2', 'node1', {})
        self.fake_hosts = [host1, host2]

    @mock.patch('nova_solverscheduler.scheduler.solvers.constraints.'
                'affinity_constraint.DifferentHostConstraint.'
                'host_filter_cls')
    def test_get_constraint_matrix(self, mock_filter_cls):
        expected_cons_mat = [
            [True, True, True],
            [False, False, False]]
        mock_filter = mock_filter_cls.return_value
        mock_filter.host_passes.side_effect = [True, False]
        cons_mat = self.constraint_cls().get_constraint_matrix(
                    self.fake_hosts, self.fake_filter_properties)
        self.assertEqual(expected_cons_mat, cons_mat)


class TestSimpleCidrAffinityConstraint(test.NoDBTestCase):

    def setUp(self):
        super(TestSimpleCidrAffinityConstraint, self).setUp()
        self.constraint_cls = affinity_constraint.SimpleCidrAffinityConstraint
        self._generate_fake_constraint_input()

    def _generate_fake_constraint_input(self):
        self.fake_filter_properties = {
                'instance_uuids': ['fake_uuid_%s' % x for x in range(3)],
                'num_instances': 3}
        host1 = fakes.FakeSolverSchedulerHostState('host1', 'node1', {})
        host2 = fakes.FakeSolverSchedulerHostState('host2', 'node1', {})
        self.fake_hosts = [host1, host2]

    @mock.patch('nova_solverscheduler.scheduler.solvers.constraints.'
                'affinity_constraint.SimpleCidrAffinityConstraint.'
                'host_filter_cls')
    def test_get_constraint_matrix(self, mock_filter_cls):
        expected_cons_mat = [
            [True, True, True],
            [False, False, False]]
        mock_filter = mock_filter_cls.return_value
        mock_filter.host_passes.side_effect = [True, False]
        cons_mat = self.constraint_cls().get_constraint_matrix(
                    self.fake_hosts, self.fake_filter_properties)
        self.assertEqual(expected_cons_mat, cons_mat)
